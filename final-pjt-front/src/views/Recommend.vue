<template>
    <div class="d-flex flex-column align-items-center">
      맞춤형 상품 추천
  
      <table class="w-100" border="1">
        <th>선택</th>
        <tr>
          <td>성별</td>
          <td>
            <label class="checkbox-label">
              <input type="checkbox" name="tendency" v-model="info.gen_two">
              <div class="checkbox-button"></div>
              <span class="checkbox-label-text">여자</span>
            </label>
            <label class="checkbox-label">
              <input type="checkbox" name="tendency" v-model="info.gen_one">
              <div class="checkbox-button"></div>
              <span class="checkbox-label-text">남자</span>
            </label>
          </td>
        </tr>
        <!-- 나머지 코드 생략 -->
      </table>
      
      <!-- 나머지 코드 생략 -->
    </div>
  </template>

  <script>
import axios from 'axios'
import DepositCard from '@/components/DepositCard.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'Recommend',
    components: {
        DepositCard
    },
    data(){
        return {
            show : false,
            sorted_depositData : [],
            info : {
            gen_one : false, gen_two : false,
            age_one : false, age_two : false, age_thr : false, age_fou : false, age_five : false, age_six : false,
            sal_one : false, sal_two : false, sal_thr : false, sal_fou : false, sal_five : false, sal_six : false,
            whl_one : false, whl_two : false, whl_thr : false, whl_fou : false, whl_five : false, whl_six : false,
            ten_one : false, ten_two : false, ten_thr : false
            },
        }
    },
    methods : {
        get_deposit_sorted() {
            const info = this.info
            axios({
                method: 'POST',
                url: `${API_URL}/deposits/recomend_deposit/`,
                data: info,
            })
            .then((response) => {
                this.sorted_depositData = response.data
                this.show = true
            })
            .catch((err) => {
            console.log(err)
            })
        }
    },
    watch : {
      info : {
        handler(val,oldval) {
            this.show = false
            this.get_deposit_sorted()
        },
        deep:true,
      }
    },
    created() {
        this.get_deposit_sorted()
    }
}

</script>
  
  <style>
  .checkbox-label {
    display: inline-block;
    margin-right: 10px;
    position: relative;
  }
  
  .checkbox-label input[type="checkbox"] {
    opacity: 0; /* 체크박스 숨기기 */
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .checkbox-button {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 1px solid #000;
    background-color: #fff;
    cursor: pointer;
    vertical-align: middle;
  }
  
  .checkbox-label-text {
    display: inline-block;
    margin-left: 5px;
    vertical-align: middle;
  }
  
  .checkbox-label input[type="checkbox"]:checked + .checkbox-button {
    background-color: #000;
  }
  </style>
  