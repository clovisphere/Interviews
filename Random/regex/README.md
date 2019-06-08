# Modify Text

Given a text, modify it in such a way that the first letter of every sentence is lowercased, 
the single space after every punction (,?:;!) is removed - and the first letter of the word that comes after the space lowercased.

e.g

```
Les trois recueils
Le premier recueil de Fables correspond aux livres I à VI des éditions actuelles.
Il est publié en 1668, dix-huit ans après les Paraphrases d'Ésope en anglais de John Ogilby, et est dédié
à un enfant, le Dauphin. Jean de La Fontaine est alors attaché, comme l'avait été sa mère, à la suite
de la Grande Madame, tante de Louis XIV qui tient sa cour au palais du Luxembourg. Il le restera jusqu'au décès de celle-ci, en 1672.
Le deuxième recueil correspond aux livres VII à XI. Il n'est publié que
dix années après le premier, en 1678 et 1679, en deux volumes, le dernier
comportant trois de ces cinq nouveaux livres.
Le poète a alors quitté depuis six ans la cour des Orléans pour le salon parisien
de Madame de La Sablière. Il dédie son tome à Madame de Montespan, favorite encore
triomphante qui, à trente sept ans, reçoit en dehors de
Versailles même, dans son nouveau et voisin château de Clagny. Quatre ans plus tôt, elle lui commandait, marque
d'estime et de protection, le livret d'un opéra qui finalement ne se fit pas.
```

becomes

```
les trois recueils
le premier recueil de Fables correspond aux livres I à VI des éditions actuelles.
il est publié en 1668,dix-huit ans après les Paraphrases d'Ésope en anglais de John Ogilby,et est dédié
à un enfant,le Dauphin.jean de La Fontaine est alors attaché,comme l'avait été sa mère,à la suite
de la Grande Madame,tante de Louis XIV qui tient sa cour au palais du Luxembourg.il le restera jusqu'au décès de celle-ci,en 1672.
le deuxième recueil correspond aux livres VII à XI.il n'est publié que
dix années après le premier,en 1678 et 1679,en deux volumes,le dernier
comportant trois de ces cinq nouveaux livres.
le poète a alors quitté depuis six ans la cour des Orléans pour le salon parisien
de Madame de La Sablière.il dédie son tome à Madame de Montespan,favorite encore
triomphante qui,à trente sept ans,reçoit en dehors de
versailles même,dans son nouveau et voisin château de Clagny.quatre ans plus tôt,elle lui commandait,marque
d'estime et de protection,le livret d'un opéra qui finalement ne se fit pas.
```

### Usage

`python3 app.py extrait_des fables_de_la_fontaine.txt`
