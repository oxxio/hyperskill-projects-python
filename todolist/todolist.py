from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Create database
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    connection = engine.connect()

    # Create table task
    Base = declarative_base()

    class Table(Base):
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String, default='default_value')
        deadline = Column(Date, default=datetime.today().date())

        def __repr__(self):
            return self.task

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    str_format = '%b'
    str_day = '%A'

    while True:

        print()
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")

        choice = int(input())
        print()

        if choice == 0:
            print("Bye!")
            break

        if choice == 1:
            today = datetime.today().date()
            # Display format ... Today 26 Apr:
            print(f'Today {today.day} {today.strftime(str_format)}:')

            rows = session.query(Table).filter(Table.deadline == today).all()
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                count = 1
                # Display all tasks for current day
                for val in range(len(rows)):
                    # Display format ... 1. Math homework
                    #                    2. Call my mom
                    print(f'{count}. {rows[val]}')
                    count += 1

        if choice == 2:
            today = datetime.today().date()

            # Next 7 days starts from today
            for i in range(0, 8):
                # Count for the next 7 days starting from Today
                next_day = today + timedelta(days=i)

                # Display format ... Sunday 26 Apr:
                print(f'{next_day.strftime(str_day)} {next_day.day} {next_day.strftime(str_format)}:')

                rows = session.query(Table).filter(Table.deadline == next_day).all()
                if len(rows) == 0:
                    print("Nothing to do!")
                else:
                    count = 1
                    # Display all tasks for current day
                    for val in range(len(rows)):
                        # Display format ... 1. Math homework
                        #                    2. Call my mom
                        print(f'{count}. {rows[val]}')
                        count += 1
                print()

        if choice == 3:
            print("All tasks:")

            rows = session.query(Table).order_by(Table.deadline).all()
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                count = 1
                # Display all tasks for current day
                for val in range(len(rows)):
                    in_date = rows[val].deadline
                    # Display format ... 1. Meet my friends. 28 Apr
                    #                    2. Math homework. 30 Apr
                    #                    3. Call my mom. 30 Apr
                    #                    4. Order a new keyboard. 1 May
                    print(f'{count}. {rows[val]}. {in_date.day} {in_date.strftime(str_format)}')
                    count += 1

        if choice == 4:
            # Missing tasks
            print("Missed tasks:")

            rows = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                count = 1
                # Display all tasks for current day
                for val in range(len(rows)):
                    in_date = rows[val].deadline
                    # Display format ... 1. Meet my friends. 28 Apr
                    #                    2. Math homework. 30 Apr
                    #                    3. Call my mom. 30 Apr
                    #                    4. Order a new keyboard. 1 May
                    print(f'{count}. {rows[val]}. {in_date.day} {in_date.strftime(str_format)}')
                    count += 1

        if choice == 5:
            in_task = input()

            print("Enter deadline")
            in_deadline = input()

            rows = session.query(Table).all()
            # Add new row to the database
            new_row = Table(id=len(rows),
                            task=in_task,
                            deadline=datetime.strptime(in_deadline, '%Y-%m-%d').date())
            session.add(new_row)
            session.commit()
            print("The task has been added!")

        if choice == 6:
            # Delete the task
            print("Choose the number of the task you want to delete:")

            rows = session.query(Table).order_by(Table.deadline).all()
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                count = 1
                # Display all tasks for current day
                for val in range(len(rows)):
                    in_date = rows[val].deadline
                    # Display format ... 1. Meet my friends. 28 Apr
                    #                    2. Math homework. 30 Apr
                    #                    3. Call my mom. 30 Apr
                    #                    4. Order a new keyboard. 1 May
                    print(f'{count}. {rows[val]}. {in_date.day} {in_date.strftime(str_format)}')
                    count += 1
            deleted_row = int(input())

            session.delete(rows[deleted_row - 1])
            session.commit()
            print("The task has been deleted!")