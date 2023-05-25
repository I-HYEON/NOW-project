<template>
  <div>
    <h1 class="detail-wrapper">자유게시판</h1>
    <template v-if="article">
      <div class="article-wrapper">
        <!-- <p>글 번호: {{ article.id }}</p> -->
        <!-- <p>작성자: {{ article.username }}</p> -->
        <p>제목: {{ article.title }}</p>
        <div class="content-wrapper">
          <p>내용: {{ article.content }}</p>
        </div>
        <p>작성시간: {{ formatDate(article.created_at) }}</p>
        <!-- <p>수정시간: {{ article.updated_at }}</p> -->
        <div v-if="article.username === userInfo.username" class="button-wrapper">
          <button type="button" @click="deleteArticle" class="btn btn-outline-danger mx-1">삭제하기</button>
          <router-link  :to="{ name: 'UpdateView', params: { id: article.id } }">
            <button type="button" class="btn btn-outline-primary mx-1">수정하기</button>
          
          </router-link>
        </div>
        <ArticleLike v-if="article.id" :article="article" />
        <br><br><br>
        <hr>

        <Comments v-if="article.id" :article="article" />
  
      </div>
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
    formatDate(datetime) {
      const dateObj = new Date(datetime);
      const year = dateObj.getFullYear();
      const month = ("0" + (dateObj.getMonth() + 1)).slice(-2);
      const day = ("0" + dateObj.getDate()).slice(-2);
      const hours = ("0" + dateObj.getHours()).slice(-2);
      const minutes = ("0" + dateObj.getMinutes()).slice(-2);

      return `${year}년-${month}월-${day}일 ${hours}:${minutes}`;
    },
    
  }
};
</script>

<style scoped>
.detail-wrapper {
  text-align: center; /* 내용을 가운데로 정렬 */
}

.article-wrapper {
  width: 50%;
  margin: 0 auto;
}

.button-wrapper {
  text-align: right;
}

.content-wrapper {
  max-height: 300px; /* 최대 높이 설정 */
  overflow: auto; /* 내용이 넘칠 경우 스크롤 표시 */
  word-break: break-all; /* 내용이 넘칠 경우 줄바꿈 */
}
</style>