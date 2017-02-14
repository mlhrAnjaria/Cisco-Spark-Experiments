//Check if it is valid URL. Thanks stackoverflow - http://stackoverflow.com/a/22648406/200063
function isURL(str) {
     var urlRegex = '^(?!mailto:)(?:(?:http|https|ftp)://)(?:\\S+(?::\\S*)?@)?(?:(?:(?:[1-9]\\d?|1\\d\\d|2[01]\\d|22[0-3])(?:\\.(?:1?\\d{1,2}|2[0-4]\\d|25[0-5])){2}(?:\\.(?:[0-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-4]))|(?:(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)(?:\\.(?:[a-z\\u00a1-\\uffff0-9]+-?)*[a-z\\u00a1-\\uffff0-9]+)*(?:\\.(?:[a-z\\u00a1-\\uffff]{2,})))|localhost)(?::\\d{2,5})?(?:(/|\\?|#)[^\\s]*)?$';
     var url = new RegExp(urlRegex, 'i');
     return str.length < 2083 && url.test(str);
}

function MessageHandler(context, event) {
     msg=event.message;
    var cmdArr=msg.split(" ");
    //context.console.log("cmdArr: "+cmdArr.length);
    //Command Check
    if (event.message.toLowerCase().startsWith("/add")) {
        if (cmdArr.length!=2 && isURL(cmdArr[2])) {
          var cmd=cmdArr[1];
          var url=cmdArr[2];
          //context.console.log("cmd: "+cmd+" url: "+url);
          //Put URL in DB
          context.simpledb.doPut(cmd.toLowerCase() ,"{\"url\":\""+url+"\"}");
          //context.sendResponse("cmd: "+cmd+" URL: "+url+" Added Successfully");
        } else {
          context.sendResponse("Check Syntax");
        }
    }
    else if(event.message.toLowerCase().startsWith("/get")){
        if(cmdArr.length!=1) {
            var findCmd=cmdArr[1];
            //Find in DB
            context.simpledb.doGet(findCmd.toLowerCase());
        }
    }
    else {
        context.sendResponse("Invalid Command");
    }
}
/** Functions declared below are required **/
function EventHandler(context, event) {
    /*if(! context.simpledb.botleveldata.numinstance)
        context.simpledb.botleveldata.numinstance = 0;
    numinstances = parseInt(context.simpledb.botleveldata.numinstance) + 1;
    context.simpledb.botleveldata.numinstance = numinstances;
    context.sendResponse("Thanks for adding me. You are:" + numinstances);*/
}

function HttpResponseHandler(context, event) {
    context.sendResponse(event.getresp);
}

function DbGetHandler(context, event) {
    try{
    	//Fetch from JSON
        var urldata = JSON.parse(event.dbval);
        if(urldata !== "") {
            var url = urldata.url;
            context.sendResponse("URL: "+url);
        }
        else {
            context.sendResponse("No Record Available!!");
        }
    } catch(err){
        context.sendResponse("No Record Available!!")
    }
}

function DbPutHandler(context, event) {
	//Add Daata Notification
    context.sendResponse("Record Added Successfully!!");
}