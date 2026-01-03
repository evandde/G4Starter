{%- if cookiecutter.use_hit_class == "true" -%}
#ifndef {{ cookiecutter.hit_class_name }}_h
#define {{ cookiecutter.hit_class_name }}_h 1

#include "G4VHit.hh"
#include "G4THitsCollection.hh"
#include "G4Allocator.hh"

class {{ cookiecutter.hit_class_name }} : public G4VHit
{
public:
    {{ cookiecutter.hit_class_name }}() = default;
    {{ cookiecutter.hit_class_name }}(const {{ cookiecutter.hit_class_name }}&) = default;
    ~{{ cookiecutter.hit_class_name }}() override = default;

    {{ cookiecutter.hit_class_name }}& operator=(const {{ cookiecutter.hit_class_name }}&) = default;

    G4bool operator==(const {{ cookiecutter.hit_class_name }}&) const;

    inline void* operator new(size_t);
    inline void  operator delete(void*);

    void Print() override;
};

using {{ cookiecutter.hit_class_name }}sCollection = G4THitsCollection<{{ cookiecutter.hit_class_name }}>;

extern G4ThreadLocal G4Allocator<{{ cookiecutter.hit_class_name }}>* {{ cookiecutter.hit_class_name }}Allocator;

inline void* {{ cookiecutter.hit_class_name }}::operator new(size_t)
{
    if (!{{ cookiecutter.hit_class_name }}Allocator)
        {{ cookiecutter.hit_class_name }}Allocator = new G4Allocator<{{ cookiecutter.hit_class_name }}>;
    return (void*){{ cookiecutter.hit_class_name }}Allocator->MallocSingle();
}

inline void {{ cookiecutter.hit_class_name }}::operator delete(void* hit)
{
    if (!{{ cookiecutter.hit_class_name }}Allocator) {
        {{ cookiecutter.hit_class_name }}Allocator = new G4Allocator<{{ cookiecutter.hit_class_name }}>;
    }
    {{ cookiecutter.hit_class_name }}Allocator->FreeSingle(({{ cookiecutter.hit_class_name }}*)hit);
}

#endif
{%- endif %}
