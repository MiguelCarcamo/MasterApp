export const msalConfig = {
    auth: {
      clientId: "22f237c9-f355-43ed-b799-fe1167c2b8e0",
      authority: "https://login.microsoftonline.com/03fa6430-2a3b-4a59-b916-ffb7eb0b395c", // This is a URL (e.g. https://login.microsoftonline.com/{your tenant ID})
      redirectUri: "https://arnpythondev.tegraglobal.com/",
    },
    cache: {
      cacheLocation: "sessionStorage", // This configures where your cache will be stored
      storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge
    }
  };
  
  // Add scopes here for ID token to be used at Microsoft identity platform endpoints.
  export const loginRequest = {
   scopes: ["User.Read"]
  };
  
  // Add the endpoints here for Microsoft Graph API services you'd like to use.
  export const graphConfig = {
      graphMeEndpoint: "https://graph.microsoft.com/v1.0/me"
  };