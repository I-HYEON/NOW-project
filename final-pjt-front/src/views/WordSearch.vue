<template>
  <div class="text-center">
    <h1>백과사전 검색</h1>
    <div class="input-group mb-3">
      <input type="text" class="form-control" v-model="content" @keyup.enter="wordSearch">
      <button class="btn btn-primary" type="submit" @click="wordSearch">검색</button>
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
                        <img
                            v-if="result.thumbnail"
                            :src="result.thumbnail"
                            class="card-img"
                            alt="Thumbnail"
                        >
                        <div v-else class="no-thumbnail">
                        <img src="#" alt="빈화면">
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
    components: {
    },
    data(){
        return {
            content: null,
            temp: null,
            show: false,
            results: [],
        }
    },
    methods:{
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
                console.log(err);
                this.show = false
            });
        } else {
            alert('검색어를 입력하세요.')
        }
        },
    }
}
</script>


<style>
  .text-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    height: 100vh;
  }

  .box {
    width: 30%;
  }
</style>