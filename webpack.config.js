const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/js/main.js',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
            loader: 'babel-loader',
            options: {
                presets: ['@babel/preset-env']
            }
        }
      }
    ]
  },
  resolve: {
    extensions: ['.js']
  },
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'web_app/static/js')
  }
};
