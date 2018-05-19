Vue.component('producer-form',{
    props: {
        producer:{
            type: Object,
            required: true
        },
        readonly:{
            type: Boolean,
            default: false
        },
        anime_options:{
            type: Array,
        }
    },
    delimiters: ["{$","$}"],
    template: `
        <div>
            <label class="control-label">Название производителя</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="producer.name" v-bind:disabled="readonly"/>

            <div v-if="readonly">
                <label class="control-label">Время создания записи</label>
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="producer.created_at" disabled/>

                <label class="control-label">Время обновления записи</label>
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="producer.updated_at" disabled/>
            </div>
            
            <label class="control-label">Аниме</label>
            <div v-if="readonly">
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="producer.anime_name" v-bind:disabled="readonly"/>
            </div>
            <div v-else>
                <select name="anime-list" title="" id="anime-list" v-model="producer.anime_id" class="form-control">
                    <option v-for="anime in anime_options" v-bind:value="anime.id">
                        {$ anime.canonical_title $}
                    </option>
                </select>
            </div>
        </div>
    `
});

Vue.component('category-form', {
   props: {
        category:{
            type: Object,
            required: true
        },
        readonly:{
            type: Boolean,
            default: false
        },
        anime_options:{
            type: Array,
        }
    },
    delimiters: ["{$","$}"],
    template: `
        <div>
            <label class="control-label">Название категории</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="category.title" v-bind:disabled="readonly"/>

            <label class="control-label">Описание</label>
            <textarea class="form-control" placeholder="Пусто" v-model:value="category.description" v-bind:disabled="readonly"></textarea >

            <div v-if="readonly">
                <label class="control-label">Время создания записи</label>
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="category.created_at" disabled/>

                <label class="control-label">Время обновления записи</label>
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="category.updated_at" disabled/>
            </div>
            
            <label class="control-label">Аниме</label>
            <div v-if="readonly">
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="category.anime_name" v-bind:disabled="readonly"/>
            </div>
            <div v-else>
                <select name="anime-list" title="" id="anime-list" v-model="category.anime_id" class="form-control">
                    <option v-for="anime in anime_options" v-bind:value="anime.id">
                        {$ anime.canonical_title $}
                    </option>
                </select>
            </div>
        </div>
    `
});


Vue.component('episode-form', {
    props: {
        episode:{
            type: Object,
            required: true
        },
        readonly:{
            type: Boolean,
            default: false
        },
        anime_options:{
            type: Array,
        }
    },
    delimiters: ["{$","$}"],
    template: `
        <div>
            <label class="control-label">Название эпизода</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.canonical_title" v-bind:disabled="readonly"/>

            <label class="control-label">Синопсис</label>
            <textarea class="form-control" placeholder="Пусто" v-model:value="episode.synopsis" v-bind:disabled="readonly"></textarea >
            
            <label class="control-label">Дата выпуска в эфир</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.air_date" v-bind:disabled="readonly"/>
            
            <label class="control-label">Номер сезона</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.season_number" v-bind:disabled="readonly"/>
            
            <label class="control-label">Номер эпизода</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.number" v-bind:disabled="readonly"/>
            
            <label class="control-label">Длина</label>
            <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.length" v-bind:disabled="readonly"/>
            
            <label class="control-label">Аниме</label>
            <div v-if="readonly">
                <input type="text" class="form-control" placeholder="Пусто" v-model:value="episode.anime_name" v-bind:disabled="readonly"/>
            </div>
            <div v-else>
                <select name="anime-list" title="" id="anime-list" v-model="episode.anime_id" class="form-control">
                    <option v-for="anime in anime_options" v-bind:value="anime.id">
                        {$ anime.canonical_title $}
                    </option>
                </select>
            </div>
        </div>
    `
});


Vue.component('character-form', {
            props: {
                character:{
                    type: Object,
                    required: true,
                    // validator: item => has(item, 'anime')
                },
                readonly:{
                    type: Boolean,
                    default: false
                },
                anime_options:{
                    type: Array,
                }
            },
            delimiters: ["{$","$}"],
            template: `
                <div>
                    <label class="control-label">Имя</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.name" v-bind:disabled="readonly"/>

                    <label class="control-label">Описание</label>
                    <textarea class="form-control" placeholder="Пусто" v-model:value="character.description" v-bind:disabled="readonly"></textarea >
                    
                    <div v-if="readonly">
                        <label class="control-label">Время создания записи</label>
                        <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.created_at" disabled/>
    
                        <label class="control-label">Время обновления записи</label>
                        <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.updated_at" disabled/>
                    </div>
                    
                    <label class="control-label">Аниме</label>
                    <div v-if="readonly">
                        <input type="text" class="form-control" placeholder="Пусто" v-model:value="character.anime_name" v-bind:disabled="readonly"/>
                    </div>
                    <div v-else>
                        <select name="anime-list" title="" id="anime-list" v-model="character.anime_id" class="form-control">
                            <option v-for="anime in anime_options" v-bind:value="anime.id">
                                {$ anime.canonical_title $}
                            </option>
                        </select>
                    </div>
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
                    <select type="text" class="form-control" placeholder="Пусто" v-model:value="anime.show_type" v-bind:disabled="readonly">
                        <option>TV</option>
                        <option>Movie</option>
                        <option>OVA</option>
                        <option>OWA</option>
                    </select>
                    
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
                   
                    <div v-if="readonly">
                        <label class="control-label">Время создания записи</label>
                        <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.created_at" disabled />
                        
                        <label class="control-label">Время обновления записи</label>
                        <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.updated_at" disabled />
                    
                    </div>
                    
                    <label class="control-label">Возрастной рейтинг</label>
                    <input type="text" class="form-control" placeholder="Пусто" v-model:value="anime.age_restriction" v-bind:disabled="readonly"/>
                </div>
            `
        }
);