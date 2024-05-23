module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "https://wangpython.pythonanywhere.com/",
        changeOrigin: true
      }
    }
  },

  publicPath: "/Gogroupbuy/"
};
