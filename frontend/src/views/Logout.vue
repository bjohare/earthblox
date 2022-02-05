<template>
  <div id="hero" class="container-fluid d-flex justify-content-center">
      <div class="d-flex ">
          <b-row class="d-flex align-items-center">
            <b-col>
              <b-card-group>
                <b-card no-body class="p-4">
                  <b-card-body>
                    <b-img src="img/earthbloxlogo.png" fluid-grow></b-img>
                    <p class="text-muted">Are you sure you want to logout?</p>
                    <b-row>
                      <b-col>
                        <b-button
                          variant="primary"
                          class=""
                          @click="logout"
                        >
                          <b-icon icon="power" aria-hidden="true"></b-icon> Logout
                        </b-button>
                        </b-col>
                        <b-col>
                        <router-link :to="{name:'Register'}">
                          <b-button id="cancelLogout" variant="danger" class="ml-3">Cancel</b-button>
                        </router-link>
                      </b-col>
                      <b-col/>
                    </b-row>
                  </b-card-body>
                </b-card>
              </b-card-group>
            </b-col>
          </b-row>
      </div>
    </div>
</template>

<script>
export default {
  name: "Logout",
  methods: {
    logout() {
      this.$store.dispatch("postLogout");
      this.$root.$emit('logout');
      this.$router.replace("/");
    }
  }
};
</script>

<style lang="scss" scoped>
#hero {
  background-image: url("assets/login-drone-1.jpg");
  background-size: cover;
  height: 100vh;
}
#cancelLogout {
  margin-left: 10px;
}
</style>
