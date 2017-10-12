/**
 * Created by jyq on 2017/10/12.
 */
const markdown = require('nunjucks-markdown');

module.exports = function(env) {
    markdown.register(env);
}