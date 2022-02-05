<template>
  <div>
    <multiselect id="datatypes" v-model="selections" :options="options" track-by="code" label="label"
    :allow-empty="false" :multiple="true"
    :close-on-select="true"
    >
      <template slot="placeholder" class="placeholder"><span class="text-muted">Select data collection types</span></template>
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
    }
  },
  components: {
    Multiselect
  },
  data() {
    return {
      options: [
        {code: 'GP', label: 'Geotagged Photos'},
        {code: 'DP', label: 'Drone Photography'},
        {code: 'GC', label: 'Ground Control Points'},
        {code: 'DV', label: 'Drone Video'},
        {code: 'DL', label: 'Drone Lidar'},
        {code: 'DR', label: 'Drone Radar'},
        {code: 'AV', label: 'Aerial Video'},
        {code: 'AR', label: 'Aerial Radar'},
        {code: 'AL', label: 'Aerial Lidar'},
        {code: 'AP', label: 'Aerial Photo'},
        {code: 'SP', label: 'Stereo Photo'},
        {code: 'OT', label: 'Other'},
      ]
    }
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
