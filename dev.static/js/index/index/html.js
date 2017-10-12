/**
 * Created by jyq on 2017/10/12.
 */
const page = require('../../../../templates/index/index.html');
const Nunjucks = require("nunjucks");

var environment = new Nunjucks.Environment();
var template = environment.render('../../../../templates/index/index.html');
module.exports= template;