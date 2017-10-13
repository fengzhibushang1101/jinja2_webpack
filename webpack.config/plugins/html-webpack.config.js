/**
 * Created by jyq on 2017/10/13.
 */
/*
 html-webpack-plugin插件，重中之重，webpack中生成HTML的插件，
 具体可以去这里查看https://www.npmjs.com/package/html-webpack-plugin
 */
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = [
  new HtmlWebpackPlugin({ //根据模板插入css/js等生成最终HTML
      favicon: './src/img/favicon.ico', //favicon路径，通过webpack引入同时可以生成hash值
      filename: './view/index.html', //生成的html存放路径，相对于path
      template: './src/view/index.html', //html模板路径
      inject: 'body', //js插入的位置，true/'head'/'body'/false
      hash: true, //为静态资源生成hash值
      chunks: ['common', 'vendors', 'index'],//需要引入的chunk，不配置就会引入所有页面的资源
      minify: { //压缩HTML文件
          removeComments: true, //移除HTML中的注释
          collapseWhitespace: false //删除空白符与换行符
      }
  }),
  new HtmlWebpackPlugin({ //根据模板插入css/js等生成最终HTML
      filename: './template/index.html', //生成的html存放路径，相对于path
      template: './templates/index/index.html', //html模板路径
      inject: true, //js插入的位置，true/'head'/'body'/false
      hash: true, //为静态资源生成hash值
      chunks: ['index'],//需要引入的chunk，不配置就会引入所有页面的资源
      minify: { //压缩HTML文件
          removeComments: true, //移除HTML中的注释
          collapseWhitespace: false //删除空白符与换行符
      }
  }),
  new HtmlWebpackPlugin({ //根据模板插入css/js等生成最终HTML
      favicon: './src/img/favicon.ico', //favicon路径，通过webpack引入同时可以生成hash值
      filename: './view/about.html', //生成的html存放路径，相对于path
      template: './src/view/about.html', //html模板路径
      inject: true, //js插入的位置，true/'head'/'body'/false
      hash: true, //为静态资源生成hash值
      chunks: ['about', 'vendors'],//需要引入的chunk，不配置就会引入所有页面的资源
      minify: { //压缩HTML文件
          removeComments: true, //移除HTML中的注释
          collapseWhitespace: false //删除空白符与换行符
      }
  }),
]