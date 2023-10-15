use config::Config;
use secrecy::{ExposeSecret, Secret};
use serde::Deserialize;

#[derive(Deserialize, Debug)]
pub struct Settings {
    pub database: DatabaseSettings,
    pub application_port: u16,
}

// TODO: Add 2 configuration files, one for used db, one for sampledb
#[derive(Deserialize, Debug)]
pub struct DatabaseSettings {
    pub username: String,
    pub password: Secret<String>,
    pub host: String,
    pub database_name: String,
}

impl DatabaseSettings {
    pub fn connection_string(&self) -> Secret<String> {
        Secret::new(format!(
            "mongodb+srv://{}:{}@{}/{}",
            self.username,
            self.password.expose_secret(),
            self.host,
            self.database_name
        ))
    }
}

pub fn get_configuration() -> Result<Settings, config::ConfigError> {
    // Initialise our configuration reader
    Config::builder()
        // Add in `./configuration.yamml`
        .add_source(config::File::with_name("configuration"))
        .build()?
        .try_deserialize()
}
