import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path: '/hello',
            name: 'hello',
            component: () => import('../views/HelloWorld.vue'),
        },
        {
            path: '/nav',
            name: 'navbar',
            component: () => import('../components/NavBar.vue'),
        },
        {
            path: '/home',
            name: 'homePage',
            component: () => import('../views/HomePage.vue'),
        },
        {
            path: '/home/item/:itemID',
            name: 'itemDetail',
            component: () => import('../views/ItemDetail.vue'),   
        }
    ]
});

export default router;