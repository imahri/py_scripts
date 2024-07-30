

def make_writer():
    str = """
NAME = exec

SRC = $(wildcard *.cpp)

HEADER = $(wildcard *.hpp)

OBJDIR = obj/

OBJ = $(addprefix $(OBJDIR), $(SRC:.cpp=.o))

FLAGS = -Wall -Wextra -Werror  -std=c++98

all: $(OBJDIR) $(NAME)

$(OBJDIR):
\tmkdir -p $(OBJDIR)

$(NAME): $(OBJ) $(HEADER)
\tc++ $(FLAGS) $(OBJ) -o $(NAME)

$(OBJDIR)%.o: %.cpp $(HEADER)
\tc++ $(FLAGS) -c $< -o $@

clean:
\trm -rf $(OBJDIR)

fclean: clean
\trm -rf $(NAME)

re: fclean all

.PHONY: all clean fclean re
    """
    return str