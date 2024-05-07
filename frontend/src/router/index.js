import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes:[
        // {
        //     path: '/',
        //     name: 'hello',
        //     component: () => import('../views/HelloWorld.vue'),
        // },
        {
            path: '/nav',
            name: 'navbar',
            component: () => import('../components/NavBar.vue'),
        },
        {
            path: '/',
            name: 'homePage',
            component: () => import('../views/HomePage.vue'),
        },
        {
            path: '/home/item/:itemID',
            name: 'itemDetail',
            component: () => import('../views/ItemDetail.vue'),   
        },
        {
            path: '/pop',
            name: 'confirm',
            component: () => import('../components/ConfirmPop.vue'),
        },
        {
            path: '/home/item/confirm',
            name: 'confirmPage',
            component: () => import('../views/ConfirmPage.vue'),
        },
        {
            path: '/history',
            name: 'historyPage',
            component: () => import('../views/HistoryPage.vue'),
        },
    ]
});

export default router;