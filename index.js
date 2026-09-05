const {setGlobalOptions} = require("firebase-functions");
const {onRequest} = require("firebase-functions/https");
setGlobalOptions({ maxInstances: 10 });
