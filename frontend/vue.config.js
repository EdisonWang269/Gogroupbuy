module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "https://wangpython.pythonanywhere.com/",
        changeOrigin: true,
      },
    },
    allowedHosts: "all",
    https: true,
  },

  publicPath: "/Gogroupbuy/",
};
