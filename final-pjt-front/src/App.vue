<template>
  <div class="container">
    <div>
      <nav class="main_nav navbar navbar-expand-lg">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">냥냥냥냥</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                  <router-link to="/">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                  </router-link>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <router-link to="/depositproducts">DepositProducts</router-link>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">
                    <router-link to="/article">Community</router-link>
                  </a>
                </li>
                <li v-if="isLogin" class="nav-item">
                  <a class="nav-link" href="#">
                    <router-link to="/profile">Profile</router-link>
                  </a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                  </a>
                  <ul class="dropdown-menu">
                      <li><a class="dropdown-item" href="#">Action</a></li>
                      <li><a class="dropdown-item" href="#">Another action</a></li>
                      <li><hr class="dropdown-divider"></li>
                      <li><a class="dropdown-item" href="#">Something else here</a></li>
                  </ul>
                </li>
                <li class="nav-item">
                  <a class="nav-link disabled">Disabled</a>
                </li>
              </ul>
          </div>
        </div>
      </nav>
    </div>
    <div>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
    name : 'APP',
    computed: {
    isLogin() {
        return this.$store.getters.isLogin
    },
    userInfo() {
        return this.$store.state.userInfo
    }
},
}
</script>
<style>
  .main_nav {
    background-color: #F1BFC9;
  };
</style>
