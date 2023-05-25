<template>
  <div class="text-center">
    <h1>금융용어 검색</h1>
    <img src='@/photo/png/dog.png' alt="first_img" style="width:80px; max-width:100%; height:auto;">
    <span>무엇이궁금하신가요?</span>
    <div class="input-group mb-3">
      <div class="d-flex" style="margin: 0 auto;">
        <input type="text" class="form-control w-150" v-model="content" @keyup.enter="wordSearch">
        <span class="btn mx-1 w-50" type="submit" @click="wordSearch" style="background-color: #601986; color:white;">검색</span>
      </div>
    </div>
    <div v-if="show">
      <h1>{{ temp }}에 대한 검색 결과</h1>
      <div v-if="results.display">
        <h4>검색결과 총 {{ results.total }}건 중 상위{{ results.display }}개</h4>
        <div class="container">
          <div class="row">
            <div class="col-12" v-for="(result, index) in results.items" :key="index">
              <div class="card" style="width: 100%;">
                <div class="row no-gutters">
                  <div class="col-md-4">
                    <img v-if="result.thumbnail" :src="result.thumbnail" class="card-img" alt="">
                    <div v-else class="no-thumbnail">
                      <img src="#" alt="">
                    </div>
                  </div>
                  <div class="col-md-8">
                    <div class="card-body">
                      <h5 class="card-title" v-html="result.title"></h5>
                      <p class="card-text" v-html="result.description"></p>
                      <a :href="result.link" class="btn btn-primary">지식백과로 가기</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <h1>검색결과가 없습니다.</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'WordSearch',
  components: {},
  data() {
    return {
      content: null,
      temp: null,
      show: false,
      results: [],
    }
  },
  methods: {
    wordSearch() {
      const content = this.content
      this.temp = this.content
      this.content = null
      if (content) {
        axios({
          method: 'GET',
          url: `${API_URL}/search/${content}/`,
        })
          .then((response) => {
            console.log(response)
            this.results = response.data
            this.show = true
          })
          .catch((err) => {
            console.log(err)
            this.show = false
          })
      } else {
        alert('검색어를 입력하세요.')
      }
    },
  },
}
</script>

<style>
.input-group {
  margin: 0px 0px;
}

.text-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; }

.searchBar {
  width: 100%;
  display: flex;
  flex-direction: row;
}