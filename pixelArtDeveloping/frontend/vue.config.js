// eslint-disable
const static_dir = "../static";
const template_path = "../templates/index.html";
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
module.exports = {
    outputDir: process.env.NODE_ENV === "production" ? static_dir : "dist/",
    indexPath: process.env.NODE_ENV === "production" ? template_path : "index.html",
    assetsDir: "",
    publicPath: process.env.NODE_ENV === "production" ? "static" : "/",
    configureWebpack: {
        plugins: [
            new MiniCssExtractPlugin({
                filename: "[name].[contenthash].css",
                chunkFilename: "[name].[contenthash].css",
            }),
        ],
    },
};