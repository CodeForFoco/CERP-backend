'use strict'
require('./check-versions')()

process.env.NODE_ENV = 'production'

const ora = require('ora')
const rm = require('rimraf')
const path = require('path')
const chalk = require('chalk')
const webpack = require('webpack')
const config = require('../config')
const webpackConfig = require('./webpack.prod.conf')
const rimraf = require('rimraf');
const mv = require('mv');

// const fs = require('fs')

const spinner = ora('building for production...')
spinner.start()

rm(path.join(config.build.assetsRoot, config.build.assetsSubDirectory), err => {
  if (err) throw err
  webpack(webpackConfig, function (err, stats) {
    spinner.stop()
    if (err) throw err
    process.stdout.write(stats.toString({
      colors: true,
      modules: false,
      children: false,
      chunks: false,
      chunkModules: false
    }) + '\n\n')

    if (stats.hasErrors()) {
      console.log(chalk.red('  Build failed with errors.\n'))
      process.exit(1)
    }

    console.log(chalk.cyan('  Build complete.\n'))
    console.log(chalk.yellow(
      '  Tip: built files are meant to be served over an HTTP server.\n' +
      '  Opening index.html over file:// won\'t work.\n'
    ))
    // fs.rename('dist/index.html', '../cerp/templates/index.html', function (err) {
    //   if (err) throw err
    //   console.log(chalk.cyan('index.html copied to new server'))
    // })
    console.log(chalk.cyan('  Custom CERP:  Moving built files into the python application'))
    console.log(chalk.cyan('  Deleting old static files...'))
    rimraf.sync('../cerp/static/css')
    rimraf.sync('../cerp/static/js')
    rimraf.sync('../cerp/templates/index.html')
    console.log(chalk.cyan('  Deleting done'))
    mv('dist/index.html', '../cerp/templates/index.html', function (err) {
      if (err) throw err
      console.log(chalk.cyan('  index.html moved to production'))
    })
    mv('dist/static/css', '../cerp/static/css', {mkdirp: true}, function (err) {
      if (err) throw err
      console.log(chalk.cyan('  css moved to production'))
    })
    mv('dist/static/js', '../cerp/static/js', {mkdirp: true}, function (err) {
      if (err) throw err
      console.log(chalk.cyan('  js moved to production'))
    })
  })
})
