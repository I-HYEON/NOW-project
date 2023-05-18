<template>
  <div>
    <form @submit.prevent="signUp">
        <label for="username">ID:</label>
        <input type="text" id="username" v-model="username">
        <br>

        <label for="password1">password1:</label>
        <input type="text" id="password1" v-model="password1">
        <br>

        <label for="password2">password confirmation:</label>
        <input type="text" id="password2" v-model="password2">

        <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
        username: '',
        password1: '',
        password2: ''
    }
  },
  methods: {
    signUp() {
        const username = this.username;
        const password1 = this.password1;
        const password2 = this.password2;

        const payload = {
            username, password1, password2
        }

        this.$store.dispatch('signUp', payload);
    }
}
}
</script>

<style>

</style>