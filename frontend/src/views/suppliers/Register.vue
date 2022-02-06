<template>
  <div id="hero" class="container-fluid d-flex justify-content-center flex-grow">
    <b-row class="d-flex align-items-start mt-2">
        <b-col class="form h-100">
            <b-card class="p-4 mb-5" v-if="!formComplete">
              <b-card-body>
                <b-img src="img/earthbloxlogo.png" fluid small></b-img>
                  <p class="text-muted">
                    Register as an Earth Blox Drone Imagery Supplier.
                  </p>
                <b-form>
                  <b-alert show variant="danger" v-if="formInvalid">
                    {{ formInvalidMessage }}
                  </b-alert>
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
                  <!-- Country Selector -->
                  <!-- DataType Selector -->
                  <div class="mb-2">
                    <country-selector id="countries" name="countries" v-model="countries" v-validate="'required'"></country-selector>
                    <b-form-invalid-feedback id="countries-invalid" :state="validateState('countries')">
                      Please select at least one country of opperation.
                    </b-form-invalid-feedback>
                  </div>
                  <!-- Consent checkbox -->
                  <b-input-group class="mb-2">
                    <b-form-checkbox
                      name="consent"
                      v-validate="'required:true'"
                      v-model="consent"
                    >
                      <span class="text-muted"> I agree to the Earth Blox data retention policy.</span>
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
                      v-validate="'required:true'"
                      v-model="certified"
                    >
                      <span class="text-muted"> I am certified to operate drones in the selected jurisdictions.</span>
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
                        Register
                      </b-button>
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
            <b-card class="p-4" v-if="formComplete">
              <b-card-body>
                <b-img src="img/earthbloxlogo.png" fluid small></b-img>
                  <h5 class="text-muted mt-3">
                    Thank you for registering with Earth Blox as a Drone Imagery Supplier.
                  </h5>
                  <h5 class="text-muted">We will be in touch with you shortly at {{ supplier.email }}.</h5>
                  <p class="text-muted">The Earth Blox Team.</p>
              </b-card-body>
            </b-card>
        </b-col>
    </b-row>
    <router-link :to="{name:'Logout'}">
      <b-button id="logout" variant="danger" class="logout-btn ml-3">Logout</b-button>
    </router-link>
  </div>
</template>
<script>
import { ValidationMixin } from "@/components/mixins/ValidationMixin";
import DataTypeSelector   from "@/components/DataTypeSelector";
import CountrySelector from "@/components/CountrySelector"

export default {
  name: 'Register',
  mixins: [ValidationMixin],
  components: {
    "dataTypeSelector": DataTypeSelector,
    "countrySelector": CountrySelector
  },
  data() {
    return {
      company: "",
      contact: "",
      email: "",
      consent: false,
      certified: false,
      datatypes: null,
      countries: null,
      formComplete: false,
      supplier: null,
      formInvalid: false,
      formInvalidMessage: null,
    };
  },
  methods: {
    register() {
      this.$validator.validateAll().then(async () => {
        if (!this.errors.any()) {
          let datatypeCodes = [];
          let countryCodes = [];
          for(let dt of this.datatypes){
            datatypeCodes.push(dt.code);
          }
          for(let cc of this.countries){
            countryCodes.push(cc.code);
          }
          let postData = {
            "company_name": this.company,
            "contact_name": this.contact,
            "email": this.email,
            "datatypes": datatypeCodes,
            "countries": countryCodes,
            "consent": this.consent,
            "certified": this.certified
          };
            let response = await this.$store.dispatch("postSupplierData", postData);
            if (response.status == 201){
              this.supplier = response.data;
              this.formComplete = true;
            }
            else if(response.status == 400){
              this.formInvalid = true;
              this.formInvalidMessage = response.data.company_name[0];
            }
            else {
              // todo: render error component
              console.log('Error processing form.');
            }
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
  min-height: 100vh;
}
.form {
  width: 50vw;
}
.logout-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}

@media (max-width: 768px) {
  .form {
    width: 90vw;
  }
  .logout-btn {
    display: none;
  }
}

@media (max-width: 1024px) {
  .form {
    width: 80vw;
  }
}
</style>
