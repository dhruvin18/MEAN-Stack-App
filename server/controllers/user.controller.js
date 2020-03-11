const mongoose=require('mongoose');
const User=mongoose.model('User');  
const passport=require('passport');
const _ =require('lodash');
// for keyword extraction Module and API KEY 
const MonkeyLearn = require('monkeylearn')
const ml = new MonkeyLearn('74792b69aa6f8594a31fb07a2b3eaa7998802f7f')


module.exports.register = (req,res,next)=> {
    console.log('Inside user Register Function');
    var user =new User();
    console.log(req.body);
    user.fullname=req.body.fullname;
    user.email=req.body.email; 
    user.password=req.body.password;

    user.save((err,doc) => {
        if(!err)
            res.send(doc);
        else{
            console.log(err);
            if(err.code == 11000){
                res.status(422).send(['Duplicate Email Addresss found']);
            }
            else{
                return next(err);
            }
        }
    }); 
}

module.exports.authenticate = (req,res,next)=> {
    console.log('Inside Login Function');
    passport.authenticate('local',(err,user,info) => {
        if(err)
            return res.status(400).json(err);
        else if(user){
            console.log('success');
            return res.status(200).json({ "token": user.generateJwt() });
        }
        else
            return res.status(404).json(info);
    })(req,res);
}

module.exports.userProfile = (req,res,next)=>{
    User.findOne({_id: req._id},
        (err, user) => {
            if(!user){
                return res.status(404).json({status: false, message: 'User Record Not found.'});
            }
            else{
                return res.status(200).json({status: true, user: _.pick(user,['fullname','email']) });
            }
        }    
    )
}

// module.exports.extract = (req,res,next) => {
//     Console.log('Inside Extraction Function');
//     let model_id = 'ex_YCya9nrn'
//     let data= [''];
//     data.append(req.body.data);
//     ml.extractors.extract(model_id, data).then(res => {
//         console.log(res.body)
//     })
//     return next(res.body);
// }

module.exports.extract = () => {
    Console.log('Inside Extracction Function');
    //res.status(200).json({"Code":"Fuckoff"});
}





