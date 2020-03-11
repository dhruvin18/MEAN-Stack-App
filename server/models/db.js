const mongoose =require('mongoose');
//MongoClient.connect(url, {useNewUrlParser: true } )
mongoose.connect("mongodb://localhost:27017/LawgicalDB", {useNewUrlParser: true, useUnifiedTopology: true,useCreateIndex: true } ,(err) => {
    if(!err){console.log('MongoDB connected');}
    else { console.log(JSON.stringify(err));}
});

require('./User.model')