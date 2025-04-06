const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: {
      main: './src/js/main.js',
      logWorkout: './src/js/pages/logWorkout.js',
      history: './src/js/pages/tracker.js',
      analysis: './src/js/analysis.js',
      dbmodels: './src/js/dbmodels.js'
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
        test: /\.css$/i,
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
            template: './src/templates/home.html',
            chunks: ['main'],  // Include specific bundles
            filename: '../../templates/home.html'        // Output file name
        }),
        new HtmlWebpackPlugin({
            template: './src/templates/log_workout.html',
            chunks: ['main', 'logWorkout'],  // Include specific bundles
            filename: '../../templates/log_workout.html'        // Output file name
        }),
        new HtmlWebpackPlugin({
            template: './src/templates/history.html',
            chunks: ['main', 'history'],  // Include specific bundles
            filename: '../../templates/history.html'        // Output file name
        }),
        new HtmlWebpackPlugin({
            template: './src/templates/analysis.html',
            chunks: ['main', 'analysis'],    // Include specific bundles
            filename: '../../templates/analysis.html'     // Output file name
        }),
        new HtmlWebpackPlugin({
            template: './src/templates/dbmodels.html',
            chunks: ['main', 'dbmodels'],    // Include specific bundles
            filename: '../../templates/dbmodels.html'     // Output file name
        })
    ],
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        compress: true,
        port: 9000
    }
  
};
