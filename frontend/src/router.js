import Vue from 'vue'
import Router from 'vue-router'

import ExampleComponent from '@/components/ExampleComponent.vue'
import Index from '@/components/Index'
import UserAuth from "@/components/UserAuth";
const routes = [
  {path: "/index", name: "index", component: Index},
  {
    path: "/create",
    name: "create",
    component: () => import("./components/ExampleComponent")
  },
  {
    path: "/auth",
    name: "auth",
    component: UserAuth
  }
]


Vue.use(Router)
const router = new Router({
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0}
  },
  mode: 'history',
  routes

})

// router.beforeEach((to, from, next) => {
//   if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
//     next()
//   } else {
//     next('/auth')
//   }
// })

export default router
