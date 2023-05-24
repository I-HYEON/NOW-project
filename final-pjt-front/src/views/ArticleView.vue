<template>
  <div>
    <h1 class="article-list">자유게시판</h1>
    <br>
    <ArticleList />
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
      // if (this.isLogin) {
      //   this.$store.dispatch('getArticles')
      // } else {
      //   alert('로그인이 필요한 페이지입니다...')
      //   this.$router.push({ name: 'loginView' })
      // } 
      this.$store.dispatch('getArticles')

    }
  }
}
</script>

<style>
.article-list {
  text-align: center;
}

</style>
