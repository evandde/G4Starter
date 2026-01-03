{%- if cookiecutter.use_hit_class == "true" -%}
#include "{{ cookiecutter.hit_class_name }}.hh"

G4ThreadLocal G4Allocator<{{ cookiecutter.hit_class_name }}>* {{ cookiecutter.hit_class_name }}Allocator = nullptr;

G4bool {{ cookiecutter.hit_class_name }}::operator==(const {{ cookiecutter.hit_class_name }}& right) const
{
    return (this == &right) ? true : false;
}

void {{ cookiecutter.hit_class_name }}::Print()
{
}
{%- endif %}
