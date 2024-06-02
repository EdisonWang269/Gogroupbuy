module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "https://wangpython.pythonanywhere.com/",
        changeOrigin: true
      }
    }
  },
    pages: {
      index: {
        entry: 'src/views/UserAll.vue',
        template: 'public/index.html',
        filename: 'homePage.html',
        title: 'Home Page',
        chunks: ['chunk-vendors', 'chunk-common', 'index'],
      },
      about: {
        entry: 'src/views/UserHistoryPage.vue',
        template: 'public/index.html',
        filename: 'history.html',
        title: 'History Page',
        chunks: ['chunk-vendors', 'chunk-common', 'about'],
      },
    },

  publicPath: "/Gogroupbuy/"
};
