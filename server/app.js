//require('./config/config');
require('./models/db');
require('./config/passportConfig');

const express=require('express');
const bodyParser=require('body-parser');
const cors=require('cors');
const rtsIndex=require('./routes/index.router');
const passport=require('passport');
//const Monkeylearn=require('monkeylearn');

var app=express()

//middleware
app.use(bodyParser.json())
app.use(cors());
app.use(passport.initialize());

app.post('/extract',function(req,response){
    console.log('Inside Extract function');
    var query = req.body.data;
    // console.log(req.body.data);
    if(query.toString() == null || query.toString() == ''){
        console.log("empty string");
        return response.status(404).json({"message": "Cannot process empty requests", "error": true});
    }
    const MonkeyLearn=require('monkeylearn');
    var data=[]
    data.push(query);
//    console.log(data[0]);
    const ml=new MonkeyLearn('6219276e44186f9d1ffa396284c6885b82f6fe6c');
    let model_id='ex_YCya9nrn';
    let keywords=[];
    ml.extractors.extract(model_id,data).then(res => {
        return response.status(200).json(res.body);
    },
    err => {
        return response.status(404).json({"message":"SOME ISSUE AT SERVER SIDE, WILL GET BACK SHORTLY."+err.errors})
    })
});

app.post('/check',function(req,res){
    res.json(req.body);
});

app.use('/api', rtsIndex);

//start server
app.listen(3000, () => console.log('Server at Port: 3000'));

//error handler
app.use((err,req,res,next)=>{
    if(err.name == 'ValidationError'){
        var valErrors = [];
        Object.keys(err.errors).forEach(key => valErrors.push(err.errors[key].message));
        res.status(422).send(valErrors);
    }
});




