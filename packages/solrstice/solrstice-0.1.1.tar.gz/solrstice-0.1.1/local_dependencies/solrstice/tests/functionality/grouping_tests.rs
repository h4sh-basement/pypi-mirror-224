use crate::structures::{get_test_data, FunctionalityTestsBuildup};
use solrstice::models::error::SolrError;
use solrstice::queries::components::grouping::{GroupFormatting, GroupingComponentBuilder};
use solrstice::queries::index::UpdateQueryBuilder;
use solrstice::queries::select::SelectQueryBuilder;
use std::collections::HashMap;

#[tokio::test]
async fn group_fields() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupBasic")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let response = SelectQueryBuilder::new()
        .fq(&["age:[* TO *]"])
        .grouping(&GroupingComponentBuilder::new().fields(&["age"]).limit(10))
        .execute(&config.context, &config.collection_name)
        .await?;
    let groups = response
        .get_groups()
        .ok_or(SolrError::Unknown("No groups found".to_string()))?;
    let age_group = groups.get("age").unwrap();
    let correct_data: HashMap<usize, usize> = [(20, 2), (40, 2), (60, 2)].iter().cloned().collect();
    for group in age_group.get_field_result().unwrap() {
        assert_eq!(
            *correct_data
                .get(&group.get_group_value::<usize>().unwrap())
                .unwrap(),
            group.doc_list.num_found
        )
    }
    let _ = config.tear_down().await;
    Ok(())
}

#[tokio::test]
async fn group_queries() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupQuery")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let response = SelectQueryBuilder::new()
        .grouping(
            &GroupingComponentBuilder::new()
                .queries(&["age:[0 TO 59]", "age:[60 TO *]"])
                .limit(10),
        )
        .execute(&config.context, &config.collection_name)
        .await?;
    let groups = response
        .get_groups()
        .ok_or(SolrError::Unknown("Could not get groups".to_string()))?;
    let first = groups
        .get("age:[0 TO 59]")
        .unwrap()
        .get_query_result()
        .unwrap();
    let second = groups
        .get("age:[60 TO *]")
        .unwrap()
        .get_query_result()
        .unwrap();
    assert_eq!(first.num_found, 4);
    assert_eq!(second.num_found, 2);
    let _ = config.tear_down().await;
    Ok(())
}

#[tokio::test]
async fn group_n_groups() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupNGroups")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let response = SelectQueryBuilder::new()
        .fq(&["age:[* TO *]"])
        .grouping(
            &GroupingComponentBuilder::new()
                .fields(&["age"])
                .limit(10)
                .n_groups(true),
        )
        .execute(&config.context, &config.collection_name)
        .await?;
    let groups = response
        .get_groups()
        .ok_or(SolrError::Unknown("Could not get groups".to_string()))?;
    let age_group = groups.get("age").unwrap();
    assert_eq!(age_group.n_groups, Some(3));
    let _ = config.tear_down().await;
    Ok(())
}

#[tokio::test]
async fn group_main() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupMain")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let result = SelectQueryBuilder::new()
        .grouping(
            &GroupingComponentBuilder::new()
                .queries(&["age:[0 TO 59]"])
                .limit(10)
                .main(true),
        )
        .execute(&config.context, &config.collection_name)
        .await?;
    let response = result.get_response().unwrap();
    let main_contents = response.get_docs::<serde_json::Value>().unwrap();
    assert_eq!(response.num_found, 4);
    assert_eq!(main_contents.len(), 4);
    let _ = config.tear_down().await;
    Ok(())
}

#[tokio::test]
async fn group_main_false() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupMainFalse")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let result = SelectQueryBuilder::new()
        .grouping(
            &GroupingComponentBuilder::new()
                .queries(&["age:[0 TO 59]"])
                .limit(10)
                .main(false),
        )
        .execute(&config.context, &config.collection_name)
        .await?;
    let response = result.get_response();
    assert!(response.is_none());
    let _ = config.tear_down().await;
    Ok(())
}

#[tokio::test]
async fn group_simple() -> Result<(), SolrError> {
    let config = FunctionalityTestsBuildup::build_up("GroupSimple")
        .await
        .unwrap();
    let update = UpdateQueryBuilder::new();
    update
        .execute(&config.context, &config.collection_name, &get_test_data())
        .await?;

    let result = SelectQueryBuilder::new()
        .grouping(
            &GroupingComponentBuilder::new()
                .fields(&["age"])
                .limit(10)
                .format(GroupFormatting::Simple),
        )
        .execute(&config.context, &config.collection_name)
        .await?;
    let response = result.get_groups().ok_or("No groups found")?;
    let group = response.get("age").ok_or("age group not found")?;
    let group_contents = group.get_simple_result().ok_or("No group contents found")?;
    assert_eq!(group_contents.num_found, 8);
    let _ = config.tear_down().await;
    Ok(())
}
