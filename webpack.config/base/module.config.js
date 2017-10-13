/**
 * Created by jyq on 2017/10/13.
 */
const dirVars = require("./dir-vars.config");
const glob = require("glob");


let options = {
    cwd: dirVars.jsDir,
    sync: true // 这里不能异步，只能同步
};
let globInstance = new glob.Glob("!(_)*", options);
console.log(globInstance.found);
module.exports = globInstance.found;