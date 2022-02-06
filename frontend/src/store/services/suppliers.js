import axios from 'axios'

let authAxios = axios.create({
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  withCredentials: true
});

const state = {
  countries: [],
};

const mutations = {
  setCountries(state, countries) {
    state.countries = countries;
  }
};

const getters = {
  getCountries(state) {
    return state.countries;
  },
};

const actions = {
  async getCountryList(context) {
    return authAxios.get('/api/suppliers/countries/')
      .then(response => {
        context.commit('setCountries', response.data)
      })
      .catch(e => { console.log(e) })
  },
  async postSupplierData(context, payload) {
    return authAxios.post('/api/suppliers/register/', payload)
      .then(response => {
        console.log('Supplier registered.')
      });
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
