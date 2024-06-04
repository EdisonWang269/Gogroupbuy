module.exports = {
  devServer: {
    allowedHosts:'all',
    https: true,
    proxy: {
      "/api": {
        target: "https://wangpython.pythonanywhere.com/",
        changeOrigin: true,
      },
    },
    
  },
   
  publicPath: "/Gogroupbuy/",
};
