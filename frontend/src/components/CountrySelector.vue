<template>
  <div>
    <multiselect id="countries" v-model="selections" :options="options" track-by="code" label="label"
    :allow-empty="true" :multiple="true"
    :close-on-select="true"
    >
      <template slot="placeholder" class="placeholder"><span class="text-muted">Select countries of operation</span></template>
    </multiselect>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect'
export default {
  props: ["value"],
  computed: {
    selections: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit('input', val);
      }
    },
    options(){
      return this.$store.getters["getCountries"];
    }
  },
  components: {
    Multiselect
  },
  methods: {
    async getCountryList(){
      await this.$store.dispatch("getCountryList");
    }
  },
  created(){
    this.getCountryList();
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
.multiselect__placeholder {
  color: #212529;
  font-weight: 400;
}
</style>
