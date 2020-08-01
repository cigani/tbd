import Vue from 'vue'
import VueRouter from 'vue-router'

import ExampleComponent from '@/components/ExampleComponent.vue'
import Index from '@/components/Index'

const routes = [
  {path: "/index", name: "index", component: Index},
  {
    path: "/create",
    name: "create",
    component: () => import("./components/ExampleComponent")
  },
]


Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0}
  },
  mode: 'history',
  routes
})


export default router
