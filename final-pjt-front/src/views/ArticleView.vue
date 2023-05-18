<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
    //   if (this.isLogin) {
    //     this.$store.dispatch('getArticles')
    //   } else {
    //     alert('로그인이 필요한 페이지입니다...')
    //     this.$router.push({ name: 'LogInView' })
    //   } 작업을 위해 잠시 주석 처리
      this.$store.dispatch('getArticles')

    }
  }
}
</script>

<style>

</style>
