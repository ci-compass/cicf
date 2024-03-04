# Configuring Amazon's DynamoDB

You may choose to do this during the lab exercise today, or you might
just choose to watch me do it and use the instance I've created. I
recommend the latter because there are umpteen dozen steps to go
through and each one of them has to be right, but it's your call. If
you're working on this later and you get stuck, send me some email and
we'll get it sorted out.

With that said, let's get started. There are two basic steps to
accomplish: get Dynamo running andv go through the security
configuration so it can be used from programs and not just the
web-based management console.

## The actual DynamoDB config *per se*

The very first step is to go to the DynamoDB console page. From
anywhere in AWS's maze of console pages, you can enter a product to
search for or you can click on "Services" to pop up a dialog of
service consoles you've used lately.

Once you've searched for the DynamoDB product and gone to that page,
click on "Create Table" to get started.

![find the right console](dynShots/01dynamoConsole.png)

You'll be prompted to enter the name for the table and you'll get to
specify the first of your columns. The "Partition key" field is
mandatory. This field is the one that is used, if need be, to split
your data among many, many servers. The other field is for a "sort
key". Partition key values don't have to be unique, but the
combination of a Partition key and a Sort key do have to be unique
across the entire table.

In our case, we've decided that name and age, together, have to be
unique for out little throwaway example.

![Are you the Keymaster?](dynShots/02createTable.png)

Scroll down to the bottom of that page and hit the "Create Table"
button.

![Create the table](dynShots/03createTableButton.png)

Clicking the "Create Table" button puts in a request to create the
table. The proces is usually very fast, taking just a handful of
seconds at the outside. You will be immediately taken to the "Tables"
view of the console, highlighted in blue on the left edge of the
browser. In the screenshot below, notice that "demoTable" is shown in
black and isn't a clickable, underlined blue thing yet. In a few
moments it will be. When it is, go ahead and click on it.

![creating the table, in process](dynShots/04newTableCreateStatus.png)

We should put some data in our new table, don't you think? Since we
clicked on "demoTable" a moment ago, we now have a view of that table
up. Click on the "Actions" button and select "Create Item".

![create an item](dynShots/05actionsCreateItem.png)

Let's add "Alice", age 28. I find it much more convenient to view the
item as regular JSON instead of the extended syntax that Amazon
provides by default. Hit the switch to go to regular JSON and fill out
the template like so:

![enter the data](dynShots/06creatingTheNewItem.png)

Click "Create Item" to actually make it happen, of course.

Now, do the same thing to add "bob", age 61.

Now, do the same thing to add "bob" again, also age 61.

Notice the error message at the bottom?

![I have a meeting with the Bobs.](dynShots/07tryToCreateBob.png)

You can't have two items with the same partition key and sort
key. But, just because we can, let's insert Bob again, but this time
with his name properly capitalized. That will be enough to
differentiate him from "bob".

Go on and click "Explore items" in the left side list of views, make
sure demoTable is selected, and note the three items now stored in our
table.

![quick little look](dynShots/08threePeopleEntered.png)

We've had enough fun with our demoTable. Let's delete it. Click on
Tables in the left sidebar, check the box for "demoTable", and then
click the "Delete" button.

![delete me](dynShots/09BackToTablesView.png)

DunamoDB will make a heroic attempt to save you from shooting yourself
in the foot. In the text box at the bottom of the popup, you'll
actually have to type "confirm" before the "Delete" button becomes
active. When it does, click it.

![no really, delete me.](dynShots/10deleteConfirmation.png)

This will take you back to the Tables view and there will be a message
indicating the deletion is in progress.

![deletion in progress](dynShots/11openSecurityCredentials.png)

The "doc-example-table-movies" table is created and populated by a
demo program that Amazon wrote, I annotated, and we ran in lab. Let's
see what is in there. You can either click on "Explore items" in the
left sidebar, or you can select the table (by checking its checkbox)
and then selecting "Explore Items" from the "Actions" pulldown. Either
way is fine.

![let's explore some](dynShots/12goToExploreItems2Ways.png)

Once we're on the "Explore items" view, we can enter the field that we
want to search and the value that we're looking for. The "condition"
pulldown gives us even more options, but for now we don't need
them. Below the entry text boxes is the "run" button. Click it.

![query by example, anyone? I thought so.](dynShots/13exploringItems.png)

After it runs, the results will be visible below the Run button. Note
that "Blazing Saddles", one of the greatest movies of all time, is one
that I added by running the demo program.

![query results](dynShots/14filterCriteriaAndResults.png)

At this point, you have a pretty good idea of how to get started with
DynamoDB. So far, though, we've only "used" the database by going
through the management console. This is useless for real-world use. If
only there was a way to manipulate Dynamo user program control...

And indeed there is (you saw it during the in-class lab activity,
remember?) Practically all of AWS's services can be manipulated
through a web-server-like control method called "web services". In
general, the interfaces are pretty easy to use. There's just one litle
catch: for security reasons, there has to be a way for the services to
know who the user is.  AWS does this by having an "Access Key" and a
"Secret Access Key".  Generating these keys is, sadly, rather
difficult the first time.

## Generating an AWS Access Key.

