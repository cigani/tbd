import Vue from 'vue'
import Vuex from 'vuex'

import users from '@/store/services/users'
import auth from '@/store/modules/auth'
import flavors from './modules/flavors/index'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    users,
    auth,
    flavors
  }
})

export default store
