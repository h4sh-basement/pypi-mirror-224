use dyn_clone::DynClone;
use reqwest::RequestBuilder;

/// Modifies a reqwest::RequestBuilder to add authentication
pub trait SolrAuth: DynClone {
    fn add_auth_to_request(&self, request: RequestBuilder) -> RequestBuilder;
}
dyn_clone::clone_trait_object!(SolrAuth);

/// Basic Authentication
/// # Examples
/// ```
/// use solrstice::models::auth::SolrBasicAuth;
/// let auth = SolrBasicAuth::new("solr", Some("SolrRocks"));
#[derive(Clone)]
pub struct SolrBasicAuth {
    pub username: String,
    pub password: Option<String>,
}

impl SolrAuth for SolrBasicAuth {
    fn add_auth_to_request(&self, request: RequestBuilder) -> RequestBuilder {
        request.basic_auth(&self.username, self.password.as_ref())
    }
}

impl SolrBasicAuth {
    /// Create a new Basic Authentication
    /// use solrstice::models::auth::SolrBasicAuth;
    /// let auth = SolrBasicAuth::new("solr", Some("SolrRocks"));
    pub fn new(username: &str, password: Option<&str>) -> SolrBasicAuth {
        SolrBasicAuth {
            username: username.to_string(),
            password: password.map(|x| x.to_string()),
        }
    }
}
