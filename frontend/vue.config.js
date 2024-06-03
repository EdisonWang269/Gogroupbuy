module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "https://wangpython.pythonanywhere.com/",
        changeOrigin: true,
      },
    },
    allowedHosts: "all",
    server: "https",
  },

  publicPath: "/Gogroupbuy/",
};
