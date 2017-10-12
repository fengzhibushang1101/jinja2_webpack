const markdown = require('nunjucks-markdown');

module.exports = function(env) {
    markdown.register(env);
}