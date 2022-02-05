<template>
  <div id="hero" class="container-fluid d-flex justify-content-center">
    <b-row class="d-flex align-items-start mt-2">
        <b-col cols="12" class="h-100">
            <b-card class="p-4">
              <b-card-body>
                <b-img src="img/earthbloxlogo.png" fluid small></b-img>
                  <p class="text-muted">
                    Register as an Earth Blox Drone Imagery Supplier.
                  </p>
                <b-form>
                  <!-- Company Name input group -->
                  <b-input-group class="mb-2">
                    <b-form-input
                      id="company-input"
                      name="company"
                      type="text"
                      class="form-control"
                      placeholder="Company Name"
                      autocomplete="company"
                      v-validate="'required'"
                      v-model="company"
                      :state="validateState('company')"
                    />
                    <b-form-invalid-feedback id="company-invalid">
                      Please enter a company name.
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <!-- Contact Name input group -->
                  <b-input-group class="mb-2">
                    <b-form-input
                      id="cotact-input"
                      name="contact"
                      type="text"
                      class="form-control"
                      placeholder="Contact Name"
                      v-validate="'required'"
                      v-model="contact"
                      :state="validateState('contact')"
                    />
                    <b-form-invalid-feedback id="contact-invalid">
                      Please enter a contact name.
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <!-- Email input group -->
                  <b-input-group class="mb-2">
                    <b-form-input
                      id="email-input"
                      name="email"
                      type="email"
                      class="form-control"
                      placeholder="Email"
                      autocomplete="email"
                      v-validate="'required|email'"
                      v-model="email"
                      :state="validateState('email')"
                    />
                    <b-form-invalid-feedback id="email-invalid">
                      Please provide a valid contact email address.
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <!-- DataType Selector -->
                  <div class="mb-2">
                    <data-type-selector id="datatypes" name="datatypes" v-model="datatypes" v-validate="'required'"></data-type-selector>
                    <b-form-invalid-feedback id="datatypes-invalid" :state="validateState('datatypes')">
                      Please select at least one drone data collection type.
                    </b-form-invalid-feedback>
                  </div>
                  <!-- Consent input group -->
                  <b-input-group class="mb-2">
                    <b-form-checkbox
                      id="consent-check"
                      name="consent"
                      class="check"
                      v-validate="'required:true'"
                      v-model="consent"
                    >
                      <span class="text-muted ml-2"> I agree to the Earth Blox data retention policy.</span>
                    </b-form-checkbox>
                    <b-form-invalid-feedback id="consent-invalid" :state="validateState('consent')">
                      {{ errors.first('consent')}}
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <!-- Consent input group -->
                  <b-input-group class="mb-2">
                    <b-form-checkbox
                      id="certified-check"
                      name="certified"
                      class="ml-5"
                      v-validate="'required:true'"
                      v-model="certified"
                    >
                      <span class="text-muted ml-2"> I am certified to operate drones in the selected jurisdictions.</span>
                    </b-form-checkbox>
                    <b-form-invalid-feedback id="certified-invalid" :state="validateState('certified')">
                      {{  errors.first('certified') }}
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <b-row>
                    <b-col cols="6">
                      <b-button
                        variant="primary"
                        class=""
                        @click="register"
                        :disabled="errors.any()"
                      >
                        <b-icon icon="power" aria-hidden="true"></b-icon> Register
                      </b-button>
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
        </b-col>
    </b-row>
    <router-link :to="{name:'Logout'}">
      <b-button id="cancelLogout" variant="danger" class="logout-btn ml-3">Logout</b-button>
    </router-link>
  </div>
</template>
<script>
import { ValidationMixin } from "@/components/mixins/ValidationMixin";
import DataTypeSelector   from "@/components/DataTypeSelector";

export default {
  name: 'Register',
  mixins: [ValidationMixin],
  components: {
    "dataTypeSelector": DataTypeSelector
  },
  data() {
    return {
      company: "",
      contact: "",
      email: "",
      consent: false,
      certified: false,
      datatypes: null,
    };
  },
  methods: {
    register() {
      this.$validator.validateAll().then(async () => {
        if (!this.errors.any()) {
          console.log('Valid registration form. Posting.');
        }
        else {
          console.log('Invalid registration form.');
        }
      });
    },
  }
}
</script>
<style scoped>
 #hero {
  background-image: url("../assets/login-drone-1.jpg");
  background-size: cover;
  height: 100vh;
}
.logout-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}
.check {
  margin-right: 1em !important
}
</style>
