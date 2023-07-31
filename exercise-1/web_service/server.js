import express from 'express'
import dotenv from 'dotenv'

// Routes import
import { router } from "./routes/index.js"


dotenv.config()


const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }))


/**
 *  App Configuration
 */

 app.set("view engine", "ejs");
 

 /**
 *   Routes Definitions
*/
app.use(router);


/**
 *  SERVER
 */
 app.listen(process.env.PORT, process.env.HOST);
console.log(`Listening on port:${process.env.PORT}`);







