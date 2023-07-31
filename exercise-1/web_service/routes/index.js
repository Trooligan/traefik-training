import express from 'express';
export const router = express.Router();



/**
* -------------- GET ROUTES ----------------
* "/"
*/
router.get("/", (req, res) => {
    
    return res.send("Web_service1");
})




