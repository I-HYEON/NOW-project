<template>
  <div>
    <h1>Detail</h1>
    <template v-if="article"> 
      <p>글 번호: {{ article.id }}</p>
      <p>작성자: {{ article.username }}</p>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
      <p>작성시간: {{ article.created_at }}</p>
      <p>수정시간: {{ article.updated_at }}</p>
      <button @click="deleteArticle">삭제</button>
      <router-link v-if="article.username===userInfo.username" :to="{ name: 'UpdateView', params: { id: article.id } }">
        <button>수정하기</button>
      </router-link>
      <br><br><br>

      <Comments v-if="article.id" :article="article" />
      <ArticleLike v-if="article.id" :article="article" />
    </template>
  </div>
</template>

<script>
import axios from 'axios';
import ArticleLike from '../components/ArticleLike.vue';
import Comments from '../components/Comments.vue';
const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'ArticleDetailView',
  components: {
    Comments,
    ArticleLike
  },
  data() {
    return {
      article: null
    };
  },
  computed: {
    comments() {
      return this.$store.state.comments;
    },
    userInfo() {
      return this.$store.state.userInfo
    },
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.$route.params.id}`
      })
        .then(() => {
          this.$router.push({ path: '/article' });
        });
      
    },
    
  }
};
</script>
