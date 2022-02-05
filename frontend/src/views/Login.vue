<template>
  <div id="hero" class="container-fluid d-flex justify-content-center">
      <b-row class="d-flex align-items-center">
        <b-col>
            <b-card no-body class="p-4">
              <b-card-body>
                <b-form>
                  <b-img src="img/earthbloxlogo.png" fluid></b-img>
                  <p class="text-muted">
                    Login to the Earth Blox Drone Supplier Portal
                  </p>
                  <div class="alert alert-danger" v-show="invalidLogin">
                    Invalid username or password.
                  </div>
                  <b-input-group class="mb-3">
                    <b-form-input
                      name="email"
                      type="text"
                      class="form-control"
                      placeholder="Email"
                      autocomplete="email"
                      v-validate="'required|email'"
                      v-model="email"
                      :state="validateState('email')"
                      @input="invalidLogin = false"
                    />
                    <b-form-invalid-feedback id="email">
                      {{ errors.first('email')}}
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <b-input-group class="mb-4">
                    <b-form-input
                      name="password"
                      type="password"
                      class="form-control"
                      placeholder="Password"
                      autocomplete="password"
                      v-model="password"
                      v-validate="'required'"
                      :state="validateState('password')"
                      @input="invalidLogin = false"
                    />
                    <b-form-invalid-feedback id="password">
                      {{ errors.first('password')}}
                    </b-form-invalid-feedback>
                  </b-input-group>
                  <b-row>
                    <b-col cols="6">
                      <b-button
                        variant="primary"
                        class=""
                        @click="login"
                        :disabled="errors.any()"
                      >
                        <b-icon icon="power" aria-hidden="true"></b-icon> Login
                      </b-button>
                    </b-col>
                    <b-col cols="6" class="text-right">
                      <b-button
                        variant="link"
                        to="/account/password-reset"
                        class="px-0"
                        >Forgot password?</b-button
                      >
                    </b-col>
                  </b-row>
                </b-form>
              </b-card-body>
            </b-card>
        </b-col>
      </b-row>
    </div>
</template>

<script>
import { ValidationMixin } from "@/components/mixins/ValidationMixin";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      invalidLogin: false,
    };
  },
  mixins: [ValidationMixin],
  methods: {
    async login() {
      this.$validator.validateAll().then(async () => {
        if (!this.errors.any()) {
          try {
            await this.$store.dispatch("postLogin", {
              email: this.email,
              password: this.password,
            });
            this.$router.replace(this.$route.query.redirect || "/register");
          } catch (error) {
            this.invalidLogin = true;
          }
        }
      });
    },
  },
};
</script>
<style scoped>
#hero {
  background-image: url("assets/login-drone-1.jpg");
  background-size: cover;
  height: 100vh;
}
</style>
