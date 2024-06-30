const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: {
      main: './src/js/main.js',
      tracker: './src/js/tracker.js',
      analysis: './src/js/analysis.js'
  },
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
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js']
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'web_app/static/js'),
    clean: true,
  },
    plugins: [
        new HtmlWebpackPlugin({
            template: './web_app/templates/tracker.html',
            chunks: ['main', 'tracker'],  // Include specific bundles
            filename: 'index.html'        // Output file name
        }),
        new HtmlWebpackPlugin({
            template: './web_app/templates/analysis.html',
            chunks: ['main', 'analysis'],    // Include specific bundles
            filename: 'analysis.html'     // Output file name
        })
    ],
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        compress: true,
        port: 9000
    }
  
};
