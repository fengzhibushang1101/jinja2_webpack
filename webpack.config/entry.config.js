/**
 * Created by jyq on 2017/10/11.
 */

const pages = require('./base/page.config');
const dirVars = require('./base/dir-vars.config');
let configEntries = {};
pages.forEach((path)=>configEntries[path] = dirVars.jsDir+"/"+path+"/page.js");
console.log(configEntries);
module.exports = configEntries;