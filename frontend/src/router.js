import Vue from 'vue'
import Router from 'vue-router'

import UserAuth from "@/components/UserComponenets/UserAuth";
import UserCreate from "@/components/UserComponenets/UserCreate";
import store from "@/store/userstore";
const routes = [
  {
    path: "/users",
    name: "users",
    component: () => import("./components/UserComponenets/UserView")
  },
  {
    path: "/auth",
    name: "auth",
    component: UserAuth
  },
  {
    path: "/create",
    name: "create",
    component: UserCreate,
  }
]


Vue.use(Router)
const router = new Router({
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0}
  },
  mode: 'history',
  routes,
  store

})

// router.beforeEach((to, from, next) => {
//   if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
//     next()
//   } else {
//     next('/auth')
//   }
// })

export default router
