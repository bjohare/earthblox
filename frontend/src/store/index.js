import Vue from 'vue'
import Vuex from 'vuex'

import users from '@/store/services/users'
import suppliers from "@/store/services/suppliers"
import auth from '@/store/modules/auth'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    users,
    auth,
    suppliers
  }
});

export default store;
