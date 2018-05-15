
Vue.component('character-form', {
            props: {
                character:{
                    type: Object,
                    required: true
                },
                readonly:{
                    type: Boolean,
                    default: false
                }
            },
            template: `
                <div>
                    <label class="control-label">Имя</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.name" v-bind:disabled="readonly"/>

                    <label class="control-label">Описание</label>
                    <textarea class="form-control" placeholder="Пусто" v-model:value="character.description" v-bind:disabled="readonly"></textarea >

                    <label class="control-label">Время создания записи</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.created_at" v-bind:disabled="readonly"/>

                    <label class="control-label">Время обновления записи</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.updated_at" v-bind:disabled="readonly"/>

                    <label class="control-label">Аниме</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.anime.canonical_title" v-bind:disabled="readonly"/>
                </div>
            `
        });


Vue.component('anime-form', {
            props: {
                anime:{
                    type: Object,
                    required: false,
                    default: {
                        canonical_title : '',
                        titles : '',
                        start_date : '',
                        end_date : '',

                    }
                },
                readonly:{
                    type: Boolean,
                    default: false
                }
            },
            template: `
                <div>
                    <label class="control-label">Название</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.canonical_title" v-bind:disabled="readonly"/>

                    <label class="control-label">Прочие названия</label>
                    <textarea class="form-control" placeholder="Пусто" v-model:value="anime.titles" v-bind:disabled="readonly"></textarea >

                    <label class="control-label">Дата начала показа</label>
                    <input type="text" class="form-control" placeholder="YYYY-MM-DD" v-model:value="anime.start_date" v-bind:disabled="readonly"/>

                    <label class="control-label">Дата окончания</label>
                    <input type="text" class="form-control" placeholder="YYYY-MM-DD" v-model:value="anime.end_date" v-bind:disabled="readonly"/>

                    <label class="control-label">Число эпиздов</label>
                    <input type="number" class="form-control" placeholder="Пусто" v-model:value="anime.episode_count" v-bind:disabled="readonly"/>
                    
                    <label class="control-label">Тип аниме</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.show_type" v-bind:disabled="readonly"/>
                    
                    <label class="control-label">Статус</label>
                    <select type="text" class="form-control" placeholder="Пусто" v-model:value="anime.status" v-bind:disabled="readonly">
                        <option>Finished</option>
                        <option>Ongoing</option>
                        <option>Cancelled</option>
                    </select>
                    
                    <label class="control-label">Синопсис</label>
                    <textarea type="text" class="form-control" placeholder="Пусто" v-model:value="anime.synopsis" v-bind:disabled="readonly"/>
                    
                    <label class="control-label">Имеется франчайз</label>
                    <input type="checkbox" class="form-control checkbox-inline"  v-model:value="anime.has_franchise" v-bind:disabled="readonly"/>
                    
                    <label class="control-label">Время создания записи</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.created_at" disabled/>
                    
                    <label class="control-label">Время обновления записи</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.updated_at" disabled/>
                    
                    <label class="control-label">Возрастной рейтинг</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.age_restriction" v-bind:disabled="readonly"/>
                </div>
            `
        });