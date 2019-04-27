<h1><a id="Data_Modeling_for_sparkify_startup_0"></a>Data Modeling for sparkify startup.</h1>
<p>In this project we are analyzing the data for startup called sparkify, we are working on their songs library data which is collected user activity on their new songs streaming app.</p>
<p>Tools we used are:</p>
<ul>
<li>Postgress db</li>
<li>Python for ETL</li>
<li>Jupyter notebook</li>
</ul>
<h1><a id="Schema_Tables_details_7"></a>Schema, Tables details:</h1>
<p>Fact and dimension tables were defined for a star schema with an analytic focus.</p>
<p><b>Fact Table</b><br>
    <i>songplays</i> - records in log data associated with song plays i.e. records with page NextSong songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</p>
<p><b>Dimension Tables</b><br>
<i>users</i> - users in the app user_id, first_name, last_name, gender, level</p>
<p><i>songs</i> - songs in music database song_id, title, artist_id, year, duration</p>
<p><i>artists</i> - artists in music database artist_id, name, location, lattitude, longitude</p>
<p><i>time</i> - timestamps of records in songplays broken down into specific units start_time, hour, day, week, month, year, weekday</p>
<p>Every time the for loop runs, you try to find the <code>song_id</code> and <code>artist_id</code> of the <em>current</em> song in the current row of log data. Therefore, every time the for loop runs, you will be changing the <code>song_select</code> query using placeholders. The <code>row.song</code>, <code>row.artist</code> and <code>row.length</code> will get inserted into the <code>song_select</code> query.</p>